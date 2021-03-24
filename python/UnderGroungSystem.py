class UndergroundSystem:

    def __init__(self):
        self.travel_itinary={"checkin":
                                 [],
                             "checkout":[]}
        self.avg_time = {}
        self.checkin = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travel_itinary["checkin"].append({"id":id,"stationName":stationName,"t":t})
        self.checkin[f"{id}"]={"stationName":stationName,"t":t}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.travel_itinary["checkout"].append({"id":id,"stationName":stationName,"t":t})
        startStation = self.checkin[f"{id}"]["stationName"]
        startTime = self.checkin[f"{id}"]["t"]
        if startStation not in self.avg_time:
            self.avg_time[startStation]={stationName:{"count":1,"time":t-startTime}}
        elif stationName not in self.avg_time[startStation]:
            self.avg_time[startStation][stationName]={"count":1,"time":t-startTime}
        else:
            self.avg_time[startStation][stationName]["time"] = (self.avg_time[startStation][stationName]["time"] * self.avg_time[startStation][stationName]["count"] + t - startTime)/(self.avg_time[startStation][stationName]["count"]+1)
            self.avg_time[startStation][stationName]["count"]+=1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if startStation in self.avg_time and endStation in self.avg_time[startStation]:
            return self.avg_time[startStation][endStation]["time"]
        else:
            return 0
def caller():
    obj = UndergroundSystem()
    arr1= ["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","getAverageTime","checkIn","getAverageTime","getAverageTime","checkOut"]
    arr2=[[],[37043,"K2618O72",29],[37043,"U1DTINDT",39],["K2618O72","U1DTINDT"],[779975,"K2618O72",112],[779975,"CN3K6CYM",157],["K2618O72","U1DTINDT"],[706901,"K2618O72",221],["K2618O72","CN3K6CYM"],[18036,"K2618O72",258],["K2618O72","U1DTINDT"],["K2618O72","CN3K6CYM"],[18036,"U1DTINDT",293]]
    for i in range(len(arr1)):
        if arr1[i] == "checkIn":
            print(obj.checkIn(arr2[i][0],arr2[i][1],arr2[i][2]))
        if arr1[i] == "checkOut":
            print(obj.checkOut(arr2[i][0],arr2[i][1],arr2[i][2]))
        if arr1[i] == "getAverageTime":
            print(obj.getAverageTime(arr2[i][0],arr2[i][1]))
    print(obj.avg_time)
    # param_3 = obj.getAverageTime(startStation,endStation)
caller()
