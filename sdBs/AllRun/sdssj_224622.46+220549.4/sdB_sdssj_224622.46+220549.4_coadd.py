from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[341.593583,22.097056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_224622.46+220549.4/sdB_sdssj_224622.46+220549.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_224622.46+220549.4/sdB_sdssj_224622.46+220549.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
