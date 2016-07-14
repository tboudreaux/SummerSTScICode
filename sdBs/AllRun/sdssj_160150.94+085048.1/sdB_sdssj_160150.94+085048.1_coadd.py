from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[240.46225,8.846694],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_160150.94+085048.1/sdB_sdssj_160150.94+085048.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_160150.94+085048.1/sdB_sdssj_160150.94+085048.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
