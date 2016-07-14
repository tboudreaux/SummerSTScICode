from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[119.207917,23.293472],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_075649.90+231736.5/sdB_sdssj_075649.90+231736.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_075649.90+231736.5/sdB_sdssj_075649.90+231736.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
