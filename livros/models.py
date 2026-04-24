from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=255) # nome do autor

    def __str__(self):
        return self.nome # representação em string do autor
    
class Livro(models.Model):
    titulo = models.CharField(max_length=255) # título do livro
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) # relacionamento com Autor
    isbn = models.CharField(max_length=20) # código ISBN
    paginas = models.PositiveBigIntegerField() # número de páginas (positivo)
    ano = models.PositiveBigIntegerField() # ano de publicação (positivo)

    def __str__(self):
        return self.titulo # representação em string do livro
    
