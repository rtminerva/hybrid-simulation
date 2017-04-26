import numpy as n

#Set basemap and grid
px,py=n.meshgrid(x,y)

m=Basemap(projection='merc',llcrnrlat=20,urcrnrlat=55,
   llcrnrlon=230,urcrnrlon=305,resolution='l')

X,Y=m(px,py)


#Draw Latitude Lines
#labels[left,right,top,bottom]  1=True 0=False
parallels = n.arange(0.,90,10.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10,linewidth=0.)

# Draw Longitude Lines
#labels[left,right,top,bottom]  1=True 0=False
meridians = n.arange(180.,360.,10.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10,linewidth=0)

#Draw Map
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.fillcontinents(color='grey',alpha=0.1,lake_color='aqua')

#Plot Contour lines and fill
levels=[5.0,5.1,5.2,5.3,5.4,5.6,5.7,5.8,5.9,6.0]
cs=m.contourf(px,py,thickness,levels,cmap=p.cm.RdBu,latlon=True,extend='both')
cs2=m.contour(px,py,thickness,levels,latlon=True,colors='k')

#Plot Streamlines
m.streamplot(px,py,U,V,latlon=True,color='k')

#Add Colorbar
cbar = p.colorbar(cs)
cbar.add_lines(cs2)
cbar.ax.set_ylabel('1000 hPa - 500 hPa Thickness (km)')

#Title
p.title('Geostrophic Winds with Geopotential Thickness')


p.show()