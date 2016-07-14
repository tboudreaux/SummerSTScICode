from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[307.826167,1.090503],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Bal_90600002/sdB_Bal_90600002_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Bal_90600002/sdB_Bal_90600002_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
