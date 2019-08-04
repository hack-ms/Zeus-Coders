import sched, time, os
from Schedule import schedule

def processData(projectPath):
    images= schedule.PlotGraph(projectPath)

    schedule.PostSocialMidia(images)

def main():
    projectPath = os.path.dirname(os.path.realpath(__file__))
    print(time.time())
    s = sched.scheduler(time.time, time.sleep)   
    s.enter(10, 1, schedule.ExtractData, kwargs={'projectPath': projectPath})
    s.enter(5, 2, schedule.ImportTxtToDatabase, kwargs={'projectPath': projectPath})
    s.enter(5, 2, processData, kwargs={'projectPath': projectPath})  
    s.run()
    print(time.time())
  
if __name__ == "__main__":    
    username = "lupadocidadao"
    password = "esaniagro12"

   # while True:
    main()