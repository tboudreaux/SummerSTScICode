from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[329.362833,37.671608],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_2155+374/sdB_fbs_2155+374_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_2155+374/sdB_fbs_2155+374_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
