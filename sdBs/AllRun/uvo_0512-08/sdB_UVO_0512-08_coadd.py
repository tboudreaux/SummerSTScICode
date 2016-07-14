from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[78.683208,-8.801608],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_UVO_0512-08/sdB_UVO_0512-08_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_UVO_0512-08/sdB_UVO_0512-08_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
