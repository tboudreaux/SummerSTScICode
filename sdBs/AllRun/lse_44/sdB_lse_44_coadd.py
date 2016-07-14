from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[208.170167,-48.139517],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lse_44/sdB_lse_44_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lse_44/sdB_lse_44_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
