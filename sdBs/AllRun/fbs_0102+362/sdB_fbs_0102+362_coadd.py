from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[16.203167,36.462],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_0102+362/sdB_fbs_0102+362_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_0102+362/sdB_fbs_0102+362_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
