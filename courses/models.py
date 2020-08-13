from django.db import models


class Categorie(models.Model):
	"""Categorie classify from which the course formats are derived"""
	name = models.CharField(max_length=250,default='Cours de base')
	description = models.CharField(max_length=1000, default='Cours de base')

	def __str__(self):
		return self.description

	def categorie_name(self):
		return self.name

class Course(models.Model):
	"""Course class from which the course formats are derived"""
	Categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	pub_date = models.DateTimeField('date published')
	description = models.CharField(max_length=1000)

	def __str__(self):
		return self.description

	def title_course(self):
		return self.title

	def published(self):
		return self.pub_date 

	class Meta:
		abstract = True

class Video(Course):
	"""course in video format """
	content = models.URLField(max_length=2000, null=True)


class Text_file(Course):
	""" course in text format (.docx, pdf, etc ...)"""
	content = models.BinaryField()
 

class Torrent(Course):
	""" course in Torrent format .torrent"""
	content = models.BinaryField()


# Create your models here.