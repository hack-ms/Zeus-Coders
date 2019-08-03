select top 10
NomeMunicipio,
--sum(MatriculasTotal) as MatriculasTotal,
--sum(Reprovados) as Reprovados,
ROUND(((sum(Reprovados)*100)/sum(MatriculasTotal)),2) as PorcentagemReprovados
from MatriculasConsolidadas 
group by NomeMunicipio
order by PorcentagemReprovados desc
