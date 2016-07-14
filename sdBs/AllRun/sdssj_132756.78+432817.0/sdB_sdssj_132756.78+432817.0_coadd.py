from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[201.986583,43.471389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_132756.78+432817.0/sdB_sdssj_132756.78+432817.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_132756.78+432817.0/sdB_sdssj_132756.78+432817.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()