from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[234.113458,25.427556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_153627.23+252539.2/sdB_SDSSJ910_153627.23+252539.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_153627.23+252539.2/sdB_SDSSJ910_153627.23+252539.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
