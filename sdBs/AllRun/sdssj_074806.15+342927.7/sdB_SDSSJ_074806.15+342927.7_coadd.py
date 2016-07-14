from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[117.025625,34.491028],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_074806.15+342927.7/sdB_SDSSJ_074806.15+342927.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_074806.15+342927.7/sdB_SDSSJ_074806.15+342927.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
