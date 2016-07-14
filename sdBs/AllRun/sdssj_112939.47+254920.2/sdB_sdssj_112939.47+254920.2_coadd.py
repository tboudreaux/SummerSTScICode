from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[172.414458,25.822278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_112939.47+254920.2/sdB_sdssj_112939.47+254920.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_112939.47+254920.2/sdB_sdssj_112939.47+254920.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
