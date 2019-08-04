select top(10)
NomeMunicipio,
NomeUnidadeEscolar,
MatriculasTotal,
Aprovados,
ROUND(((Aprovados*100)/MatriculasTotal),2) as Porcentagem
from MatriculasConsolidadas 
where NomeMunicipio = 'Campo Grande'
order by Porcentagem desc