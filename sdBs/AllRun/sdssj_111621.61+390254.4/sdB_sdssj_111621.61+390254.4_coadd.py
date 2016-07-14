from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[169.090042,39.048444],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_111621.61+390254.4/sdB_sdssj_111621.61+390254.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_111621.61+390254.4/sdB_sdssj_111621.61+390254.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()