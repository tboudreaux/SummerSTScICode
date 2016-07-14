from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[21.126167,6.815983],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0112+065/sdB_pg_0112+065_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0112+065/sdB_pg_0112+065_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
