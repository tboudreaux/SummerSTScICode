from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[144.028917,10.341111],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_093606.94+102028.0/sdB_sdssj_093606.94+102028.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_093606.94+102028.0/sdB_sdssj_093606.94+102028.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
