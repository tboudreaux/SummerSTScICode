from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[13.240792,40.963528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_0050+406/sdB_FBS_0050+406_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_0050+406/sdB_FBS_0050+406_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
