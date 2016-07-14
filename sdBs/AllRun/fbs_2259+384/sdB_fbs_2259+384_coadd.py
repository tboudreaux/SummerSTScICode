from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[345.407917,38.682608],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_2259+384/sdB_fbs_2259+384_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_2259+384/sdB_fbs_2259+384_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
