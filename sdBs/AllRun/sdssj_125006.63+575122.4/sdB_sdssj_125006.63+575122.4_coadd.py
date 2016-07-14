from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[192.527625,57.856222],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_125006.63+575122.4/sdB_sdssj_125006.63+575122.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_125006.63+575122.4/sdB_sdssj_125006.63+575122.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
