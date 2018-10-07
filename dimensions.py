#!/usr/bin/env python3

class DimVar(object):
	"""
	self.exponents = [M, L, T, C] <integers>
	"""
	dimensions = ['M','L','T','Q']
	SI = {
		'M':'kg',
		'L':'m',
		'T':'s',
		'Q':'C'
		}

		
	def __init__(self, *args):

		self.dimensions = DimVar.dimensions

		if args == None:
			self.exponents = (0,0,0,0)
		elif len(args) == 5:
			self.exponents = tuple(map(float,args[1:]))
			self.numerical_value = float(args[0])
		elif len(args) == 4:
			self.exponents = tuple(map(float,args))
			self.numerical_value = None
		self.units_dict = DimVar.SI
		self.units = [
				self.units_dict[self.dimensions[0]],
				self.units_dict[self.dimensions[1]],
				self.units_dict[self.dimensions[2]],
				self.units_dict[self.dimensions[3]]
				]

				
		self.display_units = False


		self.m = self.exponents[0]
		self.l = self.exponents[1]
		self.t = self.exponents[2]
		self.q = self.exponents[3]
		self.M = self.exponents[0]
		self.L = self.exponents[1]
		self.T = self.exponents[2]
		self.Q = self.exponents[3]
		self.x = self.numerical_value


	def __str__(self):
		numerical_value = "{}   ".format(self.numerical_value)
		n = numerical_value
		x = self.exponents
		d = self.dimensions
		u = self.units

		s="""	  {}	  {}	  {}	  {}
{}	{}	{}	{}	{}"""
	
		if not self.display_units:
			return s.format(x[0],x[1],x[2],x[3],n,d[0],d[1],d[2],d[3])
	
		else:
			return s.format(x[0],x[1],x[2],x[3],n,u[0],u[1],u[2],u[3])


	def __repr__(self):
		return str(self)
		

	def __mul__(self, other):
		newx = self.x*other.x
		newm = self.m+other.m
		newl = self.l+other.l
		newt = self.t+other.t
		newq = self.q+other.q

		return DimVar(newx, newm,newl, newt, newq)

