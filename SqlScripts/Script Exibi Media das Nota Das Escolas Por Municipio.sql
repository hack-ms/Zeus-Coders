select Cidade,
	convert(decimal(10,2),(sum(NotaDaEscola) / Count(NotaDaEscola))) as Media
from NotaGeral
Group By Cidade
order by Cidade
