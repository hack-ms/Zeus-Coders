select top 10 Cidade, Escola, 
convert(decimal (10,2), NotaDaEscola)
from NotaGeral
where Cidade = 'CAMPO GRANDE'
order by NotaDaEscola 