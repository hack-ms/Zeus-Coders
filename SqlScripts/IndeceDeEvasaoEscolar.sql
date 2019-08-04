select top(10)
NomeMunicipio,
sum(MatriculasTotal) as MatriculasTotal,
ROUND((((sum(Cancelados) + sum(Abandono))*100)/sum(MatriculasTotal)),2) as Porcentagem
from MatriculasConsolidadas 
group by NomeMunicipio
order by Porcentagem desc