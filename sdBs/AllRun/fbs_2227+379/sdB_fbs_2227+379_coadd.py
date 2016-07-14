from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[337.532167,38.202528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_2227+379/sdB_fbs_2227+379_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_2227+379/sdB_fbs_2227+379_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
