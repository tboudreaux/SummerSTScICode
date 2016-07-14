from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[348.83875,29.083608],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bal_90100001/sdB_bal_90100001_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bal_90100001/sdB_bal_90100001_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
