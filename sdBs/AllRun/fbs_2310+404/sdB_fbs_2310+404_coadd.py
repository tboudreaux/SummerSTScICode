from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[348.132792,40.727858],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_2310+404/sdB_fbs_2310+404_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_2310+404/sdB_fbs_2310+404_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
