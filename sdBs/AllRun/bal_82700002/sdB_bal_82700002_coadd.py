from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[210.508708,28.437806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bal_82700002/sdB_bal_82700002_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bal_82700002/sdB_bal_82700002_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
