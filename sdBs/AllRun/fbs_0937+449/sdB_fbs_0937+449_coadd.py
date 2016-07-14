from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[145.290917,44.753556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_0937+449/sdB_fbs_0937+449_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_0937+449/sdB_fbs_0937+449_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
