from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[11.339292,7.103339],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PB_6148/sdB_PB_6148_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PB_6148/sdB_PB_6148_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
