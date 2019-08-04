--Municipios com maiores indices de reprova��o Por Municipio
select TOP 10
    NomeMunicipio,
    sum(MatriculasTotal) as MatriculasTotal,
    sum(Reprovados) as Reprovados,
    ROUND(((sum(Reprovados)*100)/sum(MatriculasTotal)),2) as PorcentagemReprovados
from MatriculasConsolidadas 
group by NomeMunicipio
order by PorcentagemReprovados desc