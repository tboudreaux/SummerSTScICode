from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[177.84925,44.212194],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_1148+444/sdB_FBS_1148+444_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_1148+444/sdB_FBS_1148+444_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
