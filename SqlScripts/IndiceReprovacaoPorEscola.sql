select top(10)
NomeMunicipio,
NomeUnidadeEscolar,
MatriculasTotal,
Reprovados,
ROUND(((Reprovados*100)/MatriculasTotal),2) as Porcentagem
from MatriculasConsolidadas 
where NomeMunicipio = 'Campo Grande'
order by PorcentagemReprovados desc