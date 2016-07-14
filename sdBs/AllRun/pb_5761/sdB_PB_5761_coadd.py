from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[2.18,2.131469],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PB_5761/sdB_PB_5761_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PB_5761/sdB_PB_5761_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
