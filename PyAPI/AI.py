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


# when uploading, change importing to copying
from Astar import Astar

PriceOfCivilianShip=4000
class WaitState(Enum):
    WAITING_TO_BUY_SHIP = 1
    WAITING_TO_INSTALL_MODULE = 2


class Setting:
    # 为假则play()期间确保游戏状态不更新，为真则只保证游戏状态在调用相关方法时不更新，大致一帧更新一次
    @staticmethod
    def Asynchronous() -> bool:
        return False

    @staticmethod
    def ShipTypes() -> List[THUAI7.ShipType]:
        return [
            THUAI7.ShipType.CivilianShip,
            THUAI7.ShipType.CivilianShip,
            THUAI7.ShipType.MilitaryShip,
            THUAI7.ShipType.FlagShip,
        ]


numOfGridPerCell: Final[int] = 1000

    


WayOfShip1={"target":None,"Wormhole1":None,"Wormhole2":None,"Wormhole3":None,"Path":None}
WayOfShip2={"target":None,"Wormhole1":None,"Wormhole2":None,"Wormhole3":None,"Path":None}
WayOfShip3={"target":None,"Wormhole1":None,"Wormhole2":None,"Wormhole3":None,"Path":None}
WayOfShip4={"target":None,"Wormhole1":None,"Wormhole2":None,"Wormhole3":None,"Path":None}

Ship1Status={
    "target":[]
}

class AI(IAI):
    def __init__(self, pID: int):
        self.__playerID = pID

    def findWay(self,
                api: IShipAPI,
                target: tuple, 
                allow_diag: bool) -> List[tuple]:
        Map=api.GetFullMap()
        for x,x_line in enumerate(Map):
            for y,y_line in enumerate(x_line):
                if api.GetWormholeHp(x,y)>=9000:
                    Map[x][y]=THUAI7.PlaceType.Space
        Ship=api.GetSelfInfo()
        start=(int(Ship.x/1000),int(Ship.y/1000))
        return Astar(Map,start,target,allow_diag)



    def ShipPlay(self, api: IShipAPI) -> None:
        # 公共操作
        if self.__playerID == 1:
            # player1的操作
            Ship=api.GetSelfInfo()
            locality=(int(Ship.x/1000),int(Ship.y/1000))
            global Ship1Status
            if(Ship1Status["target"]!=[]):
                if(abs(Ship1Status["target"][0][0]-locality[0])<=1 and 
                   abs(Ship1Status["target"][0][1]-locality[1])<=1):
                    Ship1Status["target"]=self.findWay(api,Ship1Status["target"][-1],False)
                else:
                    angle_to_move=math.atan2(Ship1Status["target"][0][1]*1000-Ship.y,Ship1Status["target"][0][0]*1000-Ship.x)
                    if angle_to_move<0:
                        angle_to_move+=2*math.pi
                    time_to_move=int(math.sqrt((Ship1Status["target"][0][0]*1000-Ship.x)**2+(Ship1Status["target"][0][1]*1000-Ship.y)**2)/Ship.speed)
                    api.Move(time_to_move,angle_to_move)
                    time.sleep(time_to_move/1000)
            else:
                pass
            return
        elif self.__playerID == 2:
            # player2的操作
            api.MoveDown(100)
            return
        elif self.__playerID == 3:
            # player3的操作
            api.MoveDown(100)
            return
        elif self.__playerID == 4:
            # player4的操作
            api.MoveDown(100)
            return
        return

    def TeamPlay(self, api: ITeamAPI) -> None:
        assert self.__playerID == 0, "Team's playerID must be 0"
        # api.BuildShip(THUAI7.ShipType.CivilianShip,0)
        # 操作
        # 任何时候民用船小于2 都攒钱购买民用船
        # Ships=api.GetShips(self)
        # NumOfCivilianShip=0
        # for ship in Ships:
        #     if ship.shipType==THUAI7.ShipType.CivilianShip:
        #         NumOfCivilianShip+=1
        # if (len(Ships)<4 and NumOfCivilianShip<2):
        #     target_id=0
        #     target_money=PriceOfCivilianShip
        #     target_action=WaitState.WAITING_TO_BUY_SHIP
        #     target_stuff=THUAI7.ShipType.CivilianShip
        
        # # 通用等待过程
        # energy=api.GetEnergy()
        # if energy<target_money:
        #     time.sleep(10) 
        # else:
        #     if (target_action==WaitState.WAITING_TO_BUY_SHIP):
        #         api.BuildShip(self,target_stuff,0)  # 先默认在家生成 后面再修改
        #     elif (target_action==WaitState.WAITING_TO_INSTALL_MODULE):
        #         api.InstallModule(self,target_id,target_stuff)
        # return