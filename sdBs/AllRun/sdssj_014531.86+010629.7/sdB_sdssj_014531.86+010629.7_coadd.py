from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[26.38275,1.10825],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_014531.86+010629.7/sdB_sdssj_014531.86+010629.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_014531.86+010629.7/sdB_sdssj_014531.86+010629.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
