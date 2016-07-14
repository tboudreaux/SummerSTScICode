from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[121.683542,-7.709],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_080644.05-074232.4/sdB_sdssj_080644.05-074232.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_080644.05-074232.4/sdB_sdssj_080644.05-074232.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
