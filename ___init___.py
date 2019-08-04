import sched, time, os
from Schedule import schedule

def SelectAndPlotGraph(projectPath):
    # Podemos chamar vários scripts, mas para teste, só iremos passar um
    sqlScript = "IndiceReprovacao.sql"
    result = schedule.SelectDataFromDatabase(projectPath, sqlScript)
    schedule.PlotGraph(projectPath, result)

def main():
    projectPath = os.path.dirname(os.path.realpath(__file__))
    print(time.time())
    s.enter(10, 1, schedule.ExtractData(projectPath), args=())
    s.enter(5, 2, schedule.ImportTxtToDatabase(projectPath))
    s.enter(5, 2, SelectAndPlotGraph(projectPath))
    s.enter(5, 1, schedule.PostSocialMidia(), kwargs={'a': 'keyword'})
    s.run()
    print(time.time())
  
if __name__ == "__main__":
    s = sched.scheduler(time.time, time.sleep)
    username = "lupadocidadao"
    password = "esaniagro12"
    main()