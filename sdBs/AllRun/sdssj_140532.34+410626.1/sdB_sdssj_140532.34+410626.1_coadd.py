from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[211.38475,41.10725],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_140532.34+410626.1/sdB_sdssj_140532.34+410626.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_140532.34+410626.1/sdB_sdssj_140532.34+410626.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
