from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[13.062792,-10.662778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_BD_-11162/sdB_BD_-11162_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_BD_-11162/sdB_BD_-11162_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
