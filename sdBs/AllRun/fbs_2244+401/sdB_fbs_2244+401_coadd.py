from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[341.645208,40.405219],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_2244+401/sdB_fbs_2244+401_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_2244+401/sdB_fbs_2244+401_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
