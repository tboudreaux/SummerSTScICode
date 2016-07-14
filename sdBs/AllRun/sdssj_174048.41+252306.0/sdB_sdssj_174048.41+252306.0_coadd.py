from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[265.201708,25.385],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_174048.41+252306.0/sdB_sdssj_174048.41+252306.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_174048.41+252306.0/sdB_sdssj_174048.41+252306.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()