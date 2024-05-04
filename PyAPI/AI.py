import PyAPI.structures as THUAI7
from PyAPI.Interface import IShipAPI, ITeamAPI, IAI
from PyAPI.utils import AssistFunction
from typing import Union, Final, cast, List
from PyAPI.constants import Constants
import queue
import time
from enum import Enum
import sys
import math
import itertools
import json

# OUTPUTFILE 为aaalogs目录下log+日期+小时+分钟+.log(Windows下)
OUTPUTFILE="aaalogs\\log"+time.strftime("%Y-%m-%d-%H-%M", time.localtime())+".log"

def OUTPUT(string:str):
    with open(OUTPUTFILE,"a") as f:
        f.write(string)
        f.write("\n")

# when uploading, change importing to copying
import Astar

PriceOfCivilianShip=4000
PriceOfMilitaryShip=12000
PriceOfFlagShip=50000
SpentMoney=0

class WaitState(Enum):
    WAITING_TO_BUY_SHIP = 1
    WAITING_TO_INSTALL_MODULE = 2


class Setting:
    # 为假则play()期间确保游戏状态不更新，为真则只保证游戏状态在调用相关方法时不更新，大致一帧更新一次
    @staticmethod
    def Asynchronous() -> bool:
        return True

    @staticmethod
    def ShipTypes() -> List[THUAI7.ShipType]:
        return [
            THUAI7.ShipType.CivilianShip,
            THUAI7.ShipType.CivilianShip,
            THUAI7.ShipType.MilitaryShip,
            THUAI7.ShipType.FlagShip,
        ]


numOfGridPerCell: Final[int] = 1000

Ship1Status={
    "target":[],
    "state":1,
}

# 通信协议
# MessgaeDict={
#     "from":0,
#     "to":0,
#     "target":(x,y),}

EmptyResourcesSet=set()

class AI(IAI):
    def __init__(self, pID: int):
        self.__playerID = pID

    def findWay(self,api: IShipAPI,target: tuple, allow_diag: bool) -> List[tuple]:
        Map=api.GetFullMap()
        for x,x_line in enumerate(Map):
            for y,y_line in enumerate(x_line):
                if y_line==THUAI7.PlaceType.Wormhole:
                    if api.GetWormholeHp(x,y)>=9000:
                        Map[x][y]=THUAI7.PlaceType.Space
        # 若target不可达，寻找紧邻的可达位置作为target
        # 考虑了斜对角的情况
        if Map[target[0]][target[1]]!=THUAI7.PlaceType.Space and Map[target[0]][target[1]]!=THUAI7.PlaceType.Shadow:
            for x, y in itertools.product(range(target[0]-1,target[0]+2), range(target[1]-1,target[1]+2)):
                if (x>=0 and x<len(Map) and y>=0 and y<len(Map[0]) and 
                    (Map[x][y]==THUAI7.PlaceType.Space or Map[x][y]==THUAI7.PlaceType.Shadow)):
                    # OUTPUT("target is not reachable, new target is:\n"+str((x,y)))
                    target=(x,y)
                    break
        Ship=api.GetSelfInfo()
        start=(int(Ship.x/1000),int(Ship.y/1000))
        # OUTPUT("MAP is:\n"+str(Map)
        #         +"\nstart is:\n"+str(start)
        #         +"\ntarget is:\n"+str(target)
        #         +"\nallow_diag is:\n"+str(allow_diag))
        way= Astar.Astar(Map,start,target,allow_diag)
        # OUTPUT("way is:\n"+str(way))
        return way

    def findNearest(self,api: IShipAPI, type: THUAI7.PlaceType) -> tuple:
        # 寻找曼哈顿距离最近的目标
        Map=api.GetFullMap()
        Ship=api.GetSelfInfo()
        start=(int(Ship.x/1000),int(Ship.y/1000))
        target_list=[]
        for x,x_line in enumerate(Map):
            for y,y_line in enumerate(x_line):
                if y_line==type:
                    target_list.append((x,y))
        min_distance=sys.maxsize
        nearest_target=None
        for target in target_list:
            distance=abs(target[0]-start[0])+abs(target[1]-start[1])
            if distance<min_distance:
                if(type==THUAI7.PlaceType.Resource):
                    if (api.GetResourceState(target[0],target[1])!=0 
                        and (target not in EmptyResourcesSet)):
                        min_distance=distance
                        nearest_target=target
                    else:
                        # OUTPUT("Resource at "+str(target)+" is not available")
                        # OUTPUT("Resource State:"+str(api.GetResourceState(target[0],target[1])))
                        EmptyResourcesSet.add(target)
                        pass
                else:
                    min_distance=distance
                    nearest_target=target
                # min_distance=distance
                # nearest_target=target
        return nearest_target

    def sendDict(self,api: IShipAPI,dict: dict,playerID: int) -> bool:
        # 测试得到耗时在毫秒量级
        # time1=time.time()
        str_dict=json.dumps(dict)
        # 尝试三次发送字典
        for i in range(3):
            sendResult=api.SendMessage(playerID,str_dict)
            if(sendResult.result()==True):
                # time2=time.time()
                # OUTPUT("Time used to sendDict is:\n"+str(time2-time1))
                return True
        # time2=time.time()
        # OUTPUT("Failed to sendDict")
        # OUTPUT("Time used to try to sendDict is:\n"+str(time2-time1))
        return False

    def getDict(self,api: IShipAPI) -> dict:
        if(api.HaveMessage()):
            message=api.GetMessage()
            try:
                return json.loads(message[1])
            except:
                return None
        else:
            return None

    def ShipPlay(self, api: IShipAPI) -> None:
        if self.__playerID == 1:
            # 测试sendDict
            # self.sendDict(api,{"code":"OUTPUT(\"Code test\")"},0)
            # player1的操作
            Ship=api.GetSelfInfo()
            locality=(int(Ship.x/1000),int(Ship.y/1000))
            Map=api.GetFullMap()
            # OUTPUT("locality is:\n"+str(locality))
            # OUTPUT("Ship speed is:\n"+str(Ship.speed))
            global Ship1Status

            # Recieve Module
            while(api.HaveMessage()):
                messageDict=self.getDict(api)
                if(messageDict!=None):
                    if(messageDict["from"]==0):
                        if(messageDict["target"]!=None and messageDict["target"]!=Ship1Status["target"][-1]):
                            Ship1Status["target"]=[messageDict["target"]]
                            # OUTPUT("Recieved target is:\n"+str(Ship1Status["target"]))
                            
                    else:
                        pass
                else:
                    pass

            if(Ship1Status["target"]!=[]):
                if(abs(Ship1Status["target"][0][0]-locality[0])+abs(Ship1Status["target"][0][1]-locality[1])>1):
                    Ship1Status["target"]=self.findWay(api,Ship1Status["target"][-1],False)
                    # OUTPUT("Ship1Status[\"target\"] is:\n"+str(Ship1Status["target"]))
                else:
                    # OUTPUT("Moving, Ship1Status[\"target\"] is:\n"+str(Ship1Status["target"]))
                    angle_to_move=math.atan2(Ship1Status["target"][0][1]*1000+500-Ship.y,Ship1Status["target"][0][0]*1000+500-Ship.x)
                    if angle_to_move<0:
                        angle_to_move+=2*math.pi
                    # OUTPUT("angle_to_move is:\n"+str(angle_to_move))
                    distance_to_move=math.sqrt((Ship1Status["target"][0][0]*1000+500-Ship.x)**2+(Ship1Status["target"][0][1]*1000+500-Ship.y)**2)
                    time_to_move=int(distance_to_move/(Ship.speed/1000))
                    # OUTPUT("time_to_move is:\n"+str(time_to_move))
                    moveResult=api.Move(time_to_move,angle_to_move)
                    time.sleep(time_to_move/1000)
                    # OUTPUT("MoveResult is:\n"+str(moveResult.result()))
                    Ship_updated=api.GetSelfInfo()
                    if((Ship_updated.x-Ship1Status["target"][0][0]*1000-500)**2+(Ship_updated.y-Ship1Status["target"][0][1]*1000-500)**2<=2500):
                        Ship1Status["target"].pop(0)
                        # OUTPUT("Poped")
                    else:
                        # OUTPUT("Not Poped")
                        distance_moved=math.sqrt((Ship_updated.x-Ship.x)**2+(Ship_updated.y-Ship.y)**2)
                        if(moveResult.result()==False or distance_moved<0.2*distance_to_move):
                            OUTPUT("Move failed")
                            Ship1Status["target"]=[Ship1Status["target"][-1]]
            else:
                # OUTPUT("Ship1Status[\"target\"] is empty")
                # 如果在state1，寻找最近的资源点
                if Ship1Status["state"]==1:
                    # 如果周围紧邻资源点，挖矿
                    for x in range(locality[0]-1,locality[0]+2):
                        for y in range(locality[1]-1,locality[1]+2):
                            if (x>=0 and x<len(Map) and y>=0 and y<len(Map[0]) 
                                and Map[x][y]==THUAI7.PlaceType.Resource):
                                if(api.GetResourceState(x,y)>0):
                                    api.Produce()
                                    # OUTPUT("Produce")
                                    # OUTPUT("Resourse State:"+str(api.GetResourceState(x,y)))
                                    # OUTPUT("Resourse at:"+str((x,y))+" is available")
                                    time.sleep(1)
                                    return
                                else:
                                    OUTPUT("Emptied Resource at:"+str((x,y)))
                                    EmptyResourcesSet.add((x,y))
                    # 否则寻找最近的资源点
                    target=self.findNearest(api,THUAI7.PlaceType.Resource)
                    # OUTPUT("find nearest resource point:"+str(target))
                    if(target!=None):
                        Ship1Status["target"]=[target]
                    else:
                        Ship1Status["target"]=[]
            return
        elif self.__playerID == 2:
            # player2的操作
            return
        elif self.__playerID == 3:
            # player3的操作
            return
        elif self.__playerID == 4:
            # player4的操作
            return
        return

    def TeamPlay(self, api: ITeamAPI) -> None:
        assert self.__playerID == 0, "Team's playerID must be 0"
        global SpentMoney
        # 操作
        # 任何时候民用船小于2 都攒钱购买民用船
        OUTPUT("TeamPlay")
        Ships=api.GetShips()
        NumOfCivilianShip=0
        for ship in Ships:
            if ship.shipType==THUAI7.ShipType.CivilianShip:
                NumOfCivilianShip+=1
        if (len(Ships)<4 and NumOfCivilianShip<2):
            target_id=0
            target_money=PriceOfCivilianShip
            target_action=WaitState.WAITING_TO_BUY_SHIP
            target_stuff=THUAI7.ShipType.CivilianShip
        elif (len(Ships)<3 and NumOfCivilianShip>=2):
            target_id=0
            target_money=PriceOfMilitaryShip
            target_action=WaitState.WAITING_TO_BUY_SHIP
            target_stuff=THUAI7.ShipType.MilitaryShip
        else:
            target_id=0
            target_money=PriceOfFlagShip
            target_action=WaitState.WAITING_TO_BUY_SHIP
            target_stuff=THUAI7.ShipType.FlagShip


        # # 通用等待过程
        energy=api.GetScore() -SpentMoney
        OUTPUT("energy is:\n"+str(energy))
        if energy<target_money:
            OUTPUT("Waiting for energy")
            time.sleep(1)
        else:
            if (target_action==WaitState.WAITING_TO_BUY_SHIP):
                built=api.BuildShip(target_stuff,0)
                if built:  # 先默认在家生成 后面再修改
                    SpentMoney+=target_money
            elif (target_action==WaitState.WAITING_TO_INSTALL_MODULE):
                built=api.InstallModule(target_id,target_stuff)
                if built:
                    SpentMoney+=target_money
        return