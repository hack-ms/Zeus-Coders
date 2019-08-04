select 
NomeMunicipio,
sum(MatriculasTotal) as MatriculasTotal,
sum(Aprovados) as Aprovados,
ROUND(((sum(Aprovados)*100)/sum(MatriculasTotal)),2) as Porcentagem
from MatriculasConsolidadas 
group by NomeMunicipio
order by Porcentagem desc