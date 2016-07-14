from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[66.533292,15.141392],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_04233+1502/sdB_kuv_04233+1502_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_04233+1502/sdB_kuv_04233+1502_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
