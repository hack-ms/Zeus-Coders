--Unidades Escolares com maiores indices de reprovação por municipio
select 
NomeMunicipio,
NomeUnidadeEscolar,
MatriculasTotal,
Reprovados,
ROUND(((Reprovados*100)/MatriculasTotal),2) as PorcentagemReprovados
from MatriculasConsolidadas 
where NomeMunicipio = 'Alcinopolis'
order by PorcentagemReprovados desc

--Municipios com maiores indices de reprovação
select 
NomeMunicipio,
sum(MatriculasTotal) as MatriculasTotal,
sum(Reprovados) as Reprovados,
ROUND(((sum(Reprovados)*100)/sum(MatriculasTotal)),2) as PorcentagemReprovados
from MatriculasConsolidadas 
group by NomeMunicipio
order by PorcentagemReprovados desc

--Unidades Escolares com maiores indices de aprovação por municipio
select 
NomeMunicipio,
NomeUnidadeEscolar,
MatriculasTotal,
Aprovados,
ROUND(((Aprovados*100)/MatriculasTotal),2) as Porcentagem
from MatriculasConsolidadas 
where NomeMunicipio = 'Campo Grande'
order by Porcentagem desc


--Municipios com maiores indices de aprovação
select 
NomeMunicipio,
sum(MatriculasTotal) as MatriculasTotal,
sum(Aprovados) as Aprovados,
ROUND(((sum(Aprovados)*100)/sum(MatriculasTotal)),2) as Porcentagem
from MatriculasConsolidadas 
group by NomeMunicipio
order by Porcentagem desc
