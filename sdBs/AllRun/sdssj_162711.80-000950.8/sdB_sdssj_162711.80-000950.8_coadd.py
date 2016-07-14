from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[246.799167,0.164111],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_162711.80-000950.8/sdB_sdssj_162711.80-000950.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_162711.80-000950.8/sdB_sdssj_162711.80-000950.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
