from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[147.772292,38.261808],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_09481+3830/sdB_kuv_09481+3830_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_09481+3830/sdB_kuv_09481+3830_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
