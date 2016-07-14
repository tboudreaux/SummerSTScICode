from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[184.979417,31.662342],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_cbs_58/sdB_cbs_58_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_cbs_58/sdB_cbs_58_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
